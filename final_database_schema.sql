BEGIN;
--
-- Add field is_favorite to order
--
CREATE TABLE "new__menu_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "is_favorite" bool NOT NULL, "created_at" datetime NOT NULL, "status" varchar(50) NOT NULL, "dish_id" bigint NOT NULL REFERENCES "menu_dish" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__menu_order" ("id", "created_at", "status", "dish_id", "user_id", "is_favorite") SELECT "id", "created_at", "status", "dish_id", "user_id", 0 FROM "menu_order";
DROP TABLE "menu_order";
ALTER TABLE "new__menu_order" RENAME TO "menu_order";
CREATE INDEX "menu_order_dish_id_6cb7b3c8" ON "menu_order" ("dish_id");
CREATE INDEX "menu_order_user_id_56d83e83" ON "menu_order" ("user_id");
COMMIT;
