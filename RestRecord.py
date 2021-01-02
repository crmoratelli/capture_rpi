from flask import request
from flask_restful import Resource
from globals import FlaskAPI
from schemas import record_schema
from CaptureThr import CaptureThr
import os


class RestRecord(Resource):
    Capture = None

    def __init__(self):
        pass

    def get(self):
        cmd = request.args.get('cmd', default = None, type = int)
        fname = request.args.get('f', default = None, type = str)

        if cmd is None:
            return record_schema.dump({'status': False if RestRecord.Capture is None else RestRecord.Capture.status()})
        else:
            if cmd == 1 and os.path.exists(fname):
                return record_schema.dump({'status': False, 'msg': 'File exists'})

            if cmd == 1 and RestRecord.Capture is None:
                RestRecord.Capture = CaptureThr(fname=fname)
                RestRecord.Capture.start()
            elif cmd == 0 and RestRecord.Capture is not None:
                RestRecord.Capture.finish()
                RestRecord.Capture = None

            return record_schema.dump({'status': True if cmd == 1 else False})
    
FlaskAPI.add_resource(RestRecord, '/app/v0.1/record')