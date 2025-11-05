# Localhost Server Tutorial

Simple tutorials for running local development servers.

## Python HTTP Server

### Simple Server

```bash
# Serve current directory on port 5173
python3 -m http.server 5173

# Visit: http://localhost:5173
```

### Advanced Server with Auto-open

Run `server.py` for a server that:
- Automatically opens your browser
- Handles port conflicts
- Serves files from current or specified directory

```bash
python server.py
```

## Node.js Server

### Using serve

```bash
# Install globally
npm install -g serve

# Run server
serve -l 5173 .

# Visit: http://localhost:5173
```

### Using http-server

```bash
# Install globally
npm install -g http-server

# Run server
http-server -p 5173

# Visit: http://localhost:5173
```

## Docker Server

Run a server in Docker:

```bash
docker run -d -p 5173:5173 -v $(pwd):/app -w /app python:3.13 python -m http.server 5173
```

Visit: http://localhost:5173

## Examples

See `server.py` for a full-featured Python HTTP server example.

