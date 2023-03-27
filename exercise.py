from flask import Flask
import json
import psutil
import cpuinfo

app = Flask(__name__)


@app.route("/cpuinfo")
def get_cpu_info():
    cpu_info = {
        'nr_cpus': psutil.cpu_count(logical=False),
        'model_name': cpuinfo.get_cpu_info()['brand_raw']
    }
    return json.dumps(cpu_info)


@app.route("/meminfo")
def get_memory_info():
    mem_info = {
        'total_mb': psutil.virtual_memory()[0],
        'used_mb': psutil.virtual_memory()[3],
        'free_mb': psutil.virtual_memory()[4]
    }
    return json.dumps(mem_info)


if __name__ == '__main__':
    app.run()
