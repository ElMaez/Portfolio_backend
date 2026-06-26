
from utils import regex
from utils import x
from utils import no_cache
from icecream import ic #type: ignore
from flask import Blueprint, jsonify, request, session, redirect, render_template #type: ignore


ic.configureOutput(prefix="⋆౨ৎ˚⟡˖ ࣪ ⊹ ࣪ ˖ ⋆౨ৎ˚⟡˖ ࣪ ⊹ ࣪ ˖ ☆ﾐ(o\*･ω･)ﾉ | ", includeContext=True)


education_bp = Blueprint("education", __name__)


@education_bp.get("/api-get-all-educations")
@no_cache.no_cache
def show_educationslist():
    try:
        db, cursor = x.db()
        q = "SELECT * FROM education"

        cursor.execute(q)
        all_educations = cursor.fetchall()

        return jsonify({"educations":all_educations}), 200
    
    except Exception as ex:
        ic(ex)
        return ("ups ... ┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻"), 500
    
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()