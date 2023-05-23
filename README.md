# phila.gov Glossary and Translation Memory clean up

Use this script when you need to update parallel data or custom terminology in AWS Translate.

```
python full-clean-up.py <input.csv> <output.csv> <size>
```
Size is the number of bytes per segment (or row). Use 200 for creating a [Custom Terminology](https://us-east-1.console.aws.amazon.com/translate/home?region=us-east-1#terminology) and 1000 for adding [Parallel Data](https://us-east-1.console.aws.amazon.com/translate/home?region=us-east-1#parallel-data).