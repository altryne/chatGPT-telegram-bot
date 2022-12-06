import tempfile

import torchaudio
from speechbrain.pretrained import Tacotron2
from speechbrain.pretrained import HIFIGAN
import tempfile
from pathlib import Path

def textToSpeech(text, **kwargs):
  # Intialize TTS (tacotron2) and Vocoder (HiFIGAN)
  tacotron2 = Tacotron2.from_hparams(source="speechbrain/tts-tacotron2-ljspeech", savedir="tmpdir_tts")
  hifi_gan = HIFIGAN.from_hparams(source="speechbrain/tts-hifigan-ljspeech", savedir="tmpdir_vocoder")

  # Running the TTS
  mel_output, mel_length, alignment = tacotron2.encode_text(text)

  # Running Vocoder (spectrogram-to-waveform)
  waveforms = hifi_gan.decode_batch(mel_output)
  with tempfile.TemporaryDirectory() as tmpdir:
    torchaudio.save(tmpdir + "/output.wav", waveforms[0], 22050)
    return Path(tmpdir + "/output.wav").read_bytes()

  # temp directory
  # with tempfile.TemporaryDirectory() as tmpdir:
