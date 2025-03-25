from database import add_user, get_user

# Add a user
add_user("JohnDoe", 28, "Beginner", "Weight Loss", "Bodyweight")

# Get user
user = get_user("JohnDoe")
if user:
    print(f"✅ Found user: {user.name}, Age: {user.age}, Goal: {user.goal}, Equipment: {user.equipment}")
else:
    print("❌ User not found.")
