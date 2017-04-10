## nstack _stdlib_

A collection of useful modules and functions to import and use within in your own workflows - early in development, likely to grow and change over time.

### NStack.Utils

Basic utility functions, including,

| *Name* | *Usage* |
|--------|---------|
| ```uploadS3File : { title : Text, data : [Byte]} -> Text``` | Upload a data to an S3 bucket with the given title and return the URL |
| ```uploadS3Uuid : [Byte] -> Text``` | Upload a data to an S3 bucket with a unique name and return the URL |

#### Usage

Build the service using `nstack build`. Note, you will need a drop a file in the service directory called `credentials.json` that contains a single `json` object as follows (modify as needed),

```json
{
  "S3_ACCESS_KEY" : "...",
  "S3_SECRET_KEY" : "...",
  "BUCKET" : "uploads.demo.nstack.com"
}
```

### NStack.ImageProcess

A collection of methods for processing streams of images, including applying filters, etc.


| *Name* | *Usage* |
|--------|---------|
| ```applyFilter { filterType } : { title : Text, data : [Byte]} -> { title : Text, data : [Byte]}``` | Apply a filter to an incoming data element and return the modified image. The specific filter is configured by setting the variable `filterType` within a workflow to one of 'gotham', 'kelvin', 'lomo', 'nashville', 'toaster', or 'random' |


