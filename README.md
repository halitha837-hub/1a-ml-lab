# Find-S Algorithm

## Aim

To implement the Find-S Algorithm using Python.

## Dataset

The EnjoySport dataset contains weather conditions and whether the sport is enjoyed.

Attributes:

- Sky
- AirTemp
- Humidity
- Wind
- Water
- Forecast

Target:

- EnjoySport (Yes/No)

## Algorithm

1. Initialize the hypothesis with the most specific values.
2. Read each training example.
3. If the example is positive:
   - Update the hypothesis.
   - Replace conflicting attributes with '?'.
4. Ignore negative examples.
5. Display the final hypothesis.

## Files

- `finds.py`
- `enjoysport.csv`

## Output

Final Hypothesis:

```
['sunny', 'warm', '?', 'strong', '?', '?']
```
