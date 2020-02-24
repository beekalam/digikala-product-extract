/*
 Navicat Premium Data Transfer

 Source Server         : local@postgres
 Source Server Type    : PostgreSQL
 Source Server Version : 100004
 Source Host           : localhost:5432
 Source Catalog        : digikala
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 100004
 File Encoding         : 65001

 Date: 24/02/2020 17:26:02
*/


-- ----------------------------
-- Sequence structure for products_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "products_id_seq";
CREATE SEQUENCE "products_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Table structure for products
-- ----------------------------
DROP TABLE IF EXISTS "products";
CREATE TABLE "products" (
  "id" int8 NOT NULL DEFAULT nextval('products_id_seq'::regclass),
  "name" text COLLATE "pg_catalog"."default",
  "category" text COLLATE "pg_catalog"."default",
  "features" json,
  "product_id" int4,
  "seller" text COLLATE "pg_catalog"."default",
  "seller_price" text COLLATE "pg_catalog"."default",
  "name_from_title" text COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "products"."product_id" IS 'digikala id in url';

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "products_id_seq"
OWNED BY "products"."id";
SELECT setval('"products_id_seq"', 356, true);
