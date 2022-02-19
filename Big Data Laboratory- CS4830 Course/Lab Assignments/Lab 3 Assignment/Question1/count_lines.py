import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import GoogleCloudOptions
from apache_beam.options.pipeline_options import StandardOptions

options = PipelineOptions()
google_cloud_options = options.view_as(GoogleCloudOptions)
google_cloud_options.project = 'fabled-rookery-313610' # Enter your project ID
google_cloud_options.job_name = 'lab3'
google_cloud_options.temp_location = "gs://mm20b029/tmp"
google_cloud_options.region = "us-central1"
options.view_as(StandardOptions).runner = 'DataflowRunner'
p = beam.Pipeline(options=options)

lines = p | 'Read' >> beam.io.ReadFromText('gs://bdl2022/lines_big.txt') |'Count indicator variable' >> beam.Map(lambda x: len(x.split('\n'))) | 'Count lines' >> beam.combiners.Count.Globally() | 'Write' >> beam.io.WriteToText('gs://mm20b029/output1.txt')

result = p.run()
