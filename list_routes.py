# list_routes.py
import importlib
import sys
try:
    m = importlib.import_module("main")   # estamos usando --app-dir src ao rodar uvicorn
    app = getattr(m, "app", None)
    if not app:
        print("ERROR: 'app' not found in main.py")
        sys.exit(1)
    print("Registered routes:")
    for r in app.routes:
        print(f"{r.path}  -> {r.name}")
except Exception as e:
    import traceback
    traceback.print_exc()
    sys.exit(1)
