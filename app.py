"""FYP Project Hub — desktop app (PyWebView wrapper)"""
import threading
import time
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def run_server():
    import server
    from http.server import ThreadingHTTPServer
    httpd = ThreadingHTTPServer(("localhost", server.PORT), server.Handler)
    httpd.serve_forever()


def main():
    try:
        import webview
    except ImportError:
        print("Installing pywebview...")
        os.system(f'"{sys.executable}" -m pip install pywebview --quiet')
        import webview

    import server

    t = threading.Thread(target=run_server, daemon=True)
    t.start()
    time.sleep(1.2)

    icon_path = os.path.join(HERE, "logos", "project-organiser.svg")

    window = webview.create_window(
        title="FYP Project Hub",
        url=f"http://localhost:{server.PORT}",
        width=1320,
        height=860,
        min_size=(960, 640),
        background_color="#F4F2FF",
        text_select=False,
        easy_drag=False,
    )

    def on_closed():
        for pid in list(server.running.keys()):
            try:
                server.stop_project(pid)
            except Exception:
                pass
        os._exit(0)

    window.events.closed += on_closed
    webview.start(debug=False)


if __name__ == "__main__":
    main()
