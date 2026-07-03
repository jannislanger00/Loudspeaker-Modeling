# Measurement Protocol

## Goal

Capture synchronized input and output measurements for one or two loudspeakers
so that nonlinear distortion models can be trained and evaluated.

## Required Channels

- Electrical input after the amplifier stage.
- Microphone output in the loudspeaker near field.
- SPL or pressure meter channel if available.
- Laser vibrometer channel aimed at the membrane if available.

## Measurement Conditions

- Use a quiet room.
- Keep microphone distance and orientation fixed for a complete dataset.
- Record metadata for speaker ID, signal type, level, repetition, room notes,
  temperature notes, rest interval, and hardware configuration.
- Repeat each condition twice.
- Insert level-dependent rest intervals to reduce thermal compression effects.
- Warm up the system before the first recorded measurement.

## Signal Set

- Logarithmic sine sweeps.
- Multitone signals.
- Music excerpts.
- Speech excerpts.

## Raw Data Rule

Raw files under `data/raw/` are immutable. If a measurement is flawed, mark it
in the manifest and create a new recording instead of editing the original file.
