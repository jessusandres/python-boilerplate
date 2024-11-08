import traceback
import functions_framework

from flask import jsonify
from dotenv import load_dotenv

# Project
from src.common import timed, logger
from src.services import say_welcome, get_event_types

# Load environments variables, in production environment the ".env" file must not exists
load_dotenv()


@functions_framework.http
@timed
def main(request):
  logger.info("* * * * * * * * * Starting process * * * * * * * * *")

  try:
    say_welcome("Stranger")
    records = get_event_types()

    data = {
      "message": "Execution completed successfully",
      "records": records
    }

    logger.info(f"Job completed with value: {data}")

    # By default, calls to functions are POST so the code returned should be 201
    return jsonify(data), 201
  except Exception as e:
    logger.error('DATA_OBS_INV | Main function exception: %s', str(e))
    logger.error(traceback.print_exception(type(e), e, e.__traceback__))

    return jsonify({
      "code": 500,
      "error_msg": str(e)
    }), 500
