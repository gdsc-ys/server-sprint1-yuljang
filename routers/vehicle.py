from fastapi import APIRouter, HTTPException

from utils.data import get_connection


router = APIRouter(
    prefix="/vehicle",
    tags=["vehicle"],
)


@router.get("/{vehicle_id}")
async def read_vehicle(vehicle_id: int):
    con = get_connection()
    cur = con.execute("SELECT * FROM vehicle WHERE id = (?)", (vehicle_id,))
    row = cur.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="vehicle not found")
    return dict(row)