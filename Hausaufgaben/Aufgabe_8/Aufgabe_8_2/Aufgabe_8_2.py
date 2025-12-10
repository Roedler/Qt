import sys
import math
from PySide6.QtCore import QObject, QThread, Slot, Signal, QCoreApplication


class Worker(QObject):
    worker_order = ""
    finished = Signal()

    def __init__(self, id: int, parent: QObject = None):
        super().__init__(parent)

        self.id = str(id)

        print(f"[Worker {self.id}]: Objekt erzeugt.")

    @Slot()
    def work(self):
        print(f"[Worker {self.id}]: Arbeitsmethode aufgerufen.")

        LOOP_COUNT = 100
        result = 0.0

        for i in range(LOOP_COUNT):
            Worker.worker_order += self.id

            # Sinus berechnung
            for j in range(100_000):
                result += math.sin(j / 1000.0)

        QThread.currentThread().quit()
        self.finished.emit()
        print(f"[Worker {self.id}]: Arbeit beendet und Thread-Event-Loop beendet.")


def main():
    app = QCoreApplication.instance()
    if app is None:
        app = QCoreApplication(sys.argv)

    NUM_WORKERS = 10
    worker_list = []
    thread_list = []

    print("-" * 50)
    print(f"Starte die Erzeugung von {NUM_WORKERS} Worker-Objekten und Threads.")
    print("-" * 50)

    for i in range(NUM_WORKERS):
        worker_id = i + 1

        worker = Worker(worker_id)
        worker_list.append(worker)

        thread = QThread()
        thread_list.append(thread)

        worker.moveToThread(thread)
        thread.started.connect(worker.work)

    print("-" * 50)
    print("Alle Worker und Threads sind erzeugt und verbunden.")
    print("-" * 50)

    print("Starte alle Threads...")
    for thread in thread_list:
        thread.start()

    print("-" * 50)
    print("Alle Threads gestartet. Warte auf Beendigung...")
    print("-" * 50)

    for thread in thread_list:
        thread.wait()
        print(f"[Main]: Thread {thread.objectName()} beendet.")

    print("-" * 50)
    print("Alle Threads sind beendet.")
    print("-" * 50)

    print(f"Gesamt-Länge der Aufzeichnungen: {len(Worker.worker_order)}")
    print(f"Auszug der ersten 200 worker_order Zeichen:")
    print(Worker.worker_order[:200])

    for worker in worker_list:
        worker.deleteLater()


if __name__ == "__main__":
    main()
