from fastapi import APIRouter
from utils.command_executor import run_command

router = APIRouter(prefix="/system", tags=["System Commands"])


@router.get("/uptime")
def get_uptime():
    return run_command(["uptime"])


@router.get("/disk")
def get_disk_usage():
    return run_command(["df", "-h"])


@router.get("/memory")
def get_memory_usage():
    return run_command(["free", "-m"])


@router.get("/user")
def get_current_user():
    return run_command(["whoami"])