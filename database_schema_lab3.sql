BEGIN;
--
-- Create model Order
--
CREATE TABLE "menu_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_at" datetime NOT NULL, "status" varchar(50) NOT NULL, "dish_id" bigint NOT NULL REFERENCES "menu_dish" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "menu_order_dish_id_6cb7b3c8" ON "menu_order" ("dish_id");
CREATE INDEX "menu_order_user_id_56d83e83" ON "menu_order" ("user_id");
COMMIT;
