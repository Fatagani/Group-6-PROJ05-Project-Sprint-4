# MongoDB Schema Design for MVC Project

## Users Collection
{
  _id: ObjectId,
  username: String,
  password_hash: String,
  email: String,
  role: String // "user" or "admin"
}

## FoodItems Collection
{
  _id: ObjectId,
  name: String,
  category: String,
  nutrients: {
    calories: Number,
    protein: Number,
    fat: Number,
    carbs: Number
  },
  created_by: ObjectId // reference to Users
}

## Categories Collection
{
  _id: ObjectId,
  name: String,
  description: String
}

## Reports Collection
{
  _id: ObjectId,
  user_id: ObjectId,
  food_item_id: ObjectId,
  report_type: String,
  data: Object, // flexible for chart/report data
  created_at: Date
}
