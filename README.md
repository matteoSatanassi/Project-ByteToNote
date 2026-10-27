# ByteToNote

ByteToNote is a music-generation project that explores the use of a fine-tuned language model to generate melodies represented in ABC notation.

## Project Overview

The project fine-tunes `Qwen/Qwen3.5-0.8B` using Low-Rank Adaptation (LoRA) on a dataset of Irish music represented in ABC notation.

The goal is to generate musical sequences from prompts containing basic musical information, such as key, time signature, and note length.

## Technologies

- Python
- PyTorch
- Hugging Face Transformers
- PEFT (LoRA)
- ABC music notation
- music21
- MIDI and audio conversion tools

## Workflow

1. Prepare and clean the musical dataset.
2. Fine-tune the base language model using LoRA.
3. Provide a musical prompt specifying parameters such as key and time signature.
4. Generate a melody in ABC notation.
5. Convert the generated notation into MIDI.
6. Render the MIDI as audio for playback.

## Repository Structure

- `irish_abc_finetune.ipynb` — notebook containing the dataset preparation, fine-tuning, and music-generation workflow.
- `audio_generation_mac.py` — audio-generation script for macOS.
- `audio_generation_windows.py` — audio-generation script for Windows.

## Documentation

For a more detailed explanation of the project's methodology, data preparation, model training, and experimental results, see the [technical report](ByteToNote_Report.pdf).

## Exploring the Project

The main workflow is available in `irish_abc_finetune.ipynb`.

You can explore the notebook to understand the data preparation, model fine-tuning, and music-generation process. Running the complete workflow may require additional dependencies and computational resources.

## Experimental Scope and Limitations

The prepared dataset contains Irish music represented in ABC notation. Due to time and computational constraints, the fine-tuning experiments used only a small subset of the available training data.

This project focused on developing an end-to-end workflow for music generation, from dataset preparation and model fine-tuning to generating ABC notation and converting musical sequences into playable audio.

Future work could explore larger training subsets, compare different training configurations, and evaluate the musical quality and structural validity of generated melodies more systematically.

## Acknowledgements

This project uses `Qwen/Qwen3.5-0.8B` as its base model and the Hugging Face Transformers and PEFT libraries.
