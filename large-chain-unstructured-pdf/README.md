# LargeChain & Unstructured PDF pipeline

## How to install
1. Create conda env from file conda create -f environment.yml
2. verify coda env: `conda env list`
3. Create new folder under conda env: `mkdir -p /path/to/conda/envs/large_chain_unstructured/etc/conda/activate.d`
4. Create script: `nano /path/to/conda/envs/large_chain_unstructured/etc/conda/activate.d/add_to_path.sh`
5. Add following content to script:
```bash
#!/bin/bash
export PATH="/Users/your-user/.local/bin:$PATH"
``` 
6. change permission for script: `chmod +x /path/to/conda/envs/large_chain_unstructured/etc/conda/activate.d/add_to_path.sh`

## How to start

Simple run: `conda activate large_chain_unstructured`

### How to update conda environment file:

Run `conda env export > environment.yml`