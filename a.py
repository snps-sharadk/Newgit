from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor
from opentelemetry.exporter.elasticsearch import ElasticsearchSpanExporter
import requests

# Create a tracer provider
tracer_provider = TracerProvider()

# Set up the Elasticsearch exporter
es_exporter = ElasticsearchSpanExporter(
    service_name="your_service_name",
    host_name="localhost",
    port=9200,
)

# Create a batch span processor and add the exporter
span_processor = BatchExportSpanProcessor(es_exporter)
tracer_provider.add_span_processor(span_processor)

# Register the tracer provider
trace.set_tracer_provider(tracer_provider)

# Get a tracer
tracer = trace.get_tracer(__name__)

# Example code to create and record a span
with tracer.start_as_current_span("example_span"):
    # Your code logic goes here
    # ...

# Flush the spans before the program exits
    span_processor.shutdown()