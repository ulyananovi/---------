BEGIN;
--
-- Create model Category
--
CREATE TABLE "menu_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
--
-- Create model Dish
--
CREATE TABLE "menu_dish" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "description" text NOT NULL, "price" decimal NOT NULL, "weight" varchar(50) NOT NULL, "image_name" varchar(100) NOT NULL, "category_id" bigint NOT NULL REFERENCES "menu_category" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "menu_dish_category_id_16b2903d" ON "menu_dish" ("category_id");
COMMIT;
