from pathlib import Path

data_dir = (Path().cwd().parents[0] / 'data').absolute()
data_raw = data_dir / 'raw'
data_processed = data_dir / 'processed'
data_mask = data_dir / 'mask'
data_meta = data_dir / 'metadata'