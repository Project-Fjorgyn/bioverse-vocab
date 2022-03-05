# bioverse-vocab
The data backend for the [app](https://github.com/Project-Fjorgyn/bioverse).

To add new vocab to the app simply run:
```bash
python build_vocab_service.py
```
and then copy the `vocab` directory to `assets` in the app and `vocab.service.js` to the vocab service in the app. Finally go to `shortcuts.context.js` and `identify.context.js` and update the `BuildTree` call and `topLevel` state to use the top level of your identification hierarchy.

To autogenerate and run the tests:
```bash
python schema_tests.py
python members_tests.py
```

Example of checking for overlap:
```bash
python check_overlap.py -d vocab/data/trees/ -o overlap.json -e exclusions.json 
```