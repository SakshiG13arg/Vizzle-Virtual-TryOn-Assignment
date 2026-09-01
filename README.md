# Vizzle Virtual Try-On Evaluation

## Objective

This project evaluates AI-based virtual try-on models for fashion
e-commerce, with emphasis on visual quality, generation speed,
cost, robustness and production suitability.

The target requirements are:

- Generation time: below 15 seconds per image
- Cost: below INR 4 per generation

## Clothing Categories

The evaluation covers:

1. Saree
2. Kurti
3. Lehenga
4. Top
5. T-shirt
6. Jumpsuit
7. Coat
8. Shirt
9. Jeans
10. Trousers

## Model Evaluation

FASHN Virtual Try-On was evaluated using a hosted inference interface.

The generated results were assessed using:

- Fit
- Drape
- Texture fidelity
- Body preservation
- Face preservation
- Artifact control

Each criterion was evaluated on a 1–10 scale for internal comparison.

## Evaluation Procedure

The same person image was used with different garment images
corresponding to the clothing categories.

For each generated result, the visual quality was inspected and the
evaluation record was stored in:

`evaluation/results.csv`

Generated examples are stored in:

`outputs/`

## Results

The detailed evaluation records are available in:

`evaluation/results.csv`

The generated virtual try-on examples are available in:

`outputs/`

The results show generally strong preservation of the person's face
and body while performance varies by garment type. Saree-style draping
was more challenging than simpler garments because of the complex
draping structure.

## Cost

The evaluation used free hosted inference, so the direct testing
expenditure was INR 0.

This does not imply zero production cost. Production deployment would
require appropriate API or GPU infrastructure.

## Latency

The assignment target is below 15 seconds per generated image.

Independent latency was not consistently recorded for every hosted
generation during this evaluation. Therefore, fabricated latency
values are not reported.

Hosted GPU quota limitations also affected repeatability.

A dedicated/API-based benchmark should be performed before production
deployment.

## Optimization Considerations

Potential optimization approaches include:

- reducing inference steps where quality permits
- model quantization
- GPU inference optimization
- selecting suitable output resolution
- reducing preprocessing overhead
- caching reusable components
- balancing image quality against latency and cost

## Production Recommendation

FASHN VTON is a promising candidate for further evaluation because it
produced usable virtual try-on results across multiple clothing types.

Before production adoption, it should be benchmarked using the intended
production infrastructure to verify:

- consistent latency below 15 seconds
- generation cost below INR 4
- visual quality across all required clothing categories
- robustness on diverse images

Model/API licensing and commercial-use terms should also be verified
before deployment.

## Limitations

The evaluation was performed using hosted inference. GPU quota and
availability limited repeated testing.

Therefore, these results should be considered an initial evaluation
rather than a production benchmark.

## Project Structure

```text
Vizzle_VTON_Assignment/
├── app.py
├── README.md
├── requirements.txt
├── evaluation/
│   └── results.csv
└── outputs/