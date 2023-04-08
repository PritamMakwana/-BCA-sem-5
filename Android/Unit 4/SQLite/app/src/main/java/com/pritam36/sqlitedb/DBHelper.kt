package com.pritam36.sqlitedb

import android.content.ContentValues
import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper

class DBHelper(context: Context, factory: SQLiteDatabase.CursorFactory?) :
    SQLiteOpenHelper(context, DATABASE_NAME, factory, DATABASE_VERSION) {
    companion object{

        private const val DATABASE_NAME = "GROCERY"
        private const val DATABASE_VERSION = 1
        const val TABLE_NAME = "grocery_list"
        const val ID_COL = "id"
        const val NAME_COl = "name"
        const val QNT_COL = "qnty"
    }
    override fun onCreate(db: SQLiteDatabase) {
        val query = ("CREATE TABLE " + TABLE_NAME + " ("
                + ID_COL + " INTEGER PRIMARY KEY, " +
                NAME_COl + " TEXT," +
                QNT_COL + " TEXT" + ")")
        db.execSQL(query)
    }
    override fun onUpgrade(db: SQLiteDatabase, p1: Int, p2: Int) {
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_NAME)
        onCreate(db)
    }
    fun setItem(name: String, qty: String) {
        val values = ContentValues()
        values.put(NAME_COl, name)
        values.put(QNT_COL, qty)
        val db = this.writableDatabase
        db.insert(TABLE_NAME, null, values)
    }
    fun getItems(): List<String>? {
        val db = this.readableDatabase
        var items = mutableListOf<String>()
        var cur = db.rawQuery("SELECT * FROM " + TABLE_NAME, null)
        if (cur.moveToFirst()) {
            while (cur.moveToNext()) {
                items.add(cur!!.getString(1))
            }
        }
        return items
    }
    fun getItem(name: String): String {
        val db = this.readableDatabase
        var cur = db.rawQuery("SELECT * FROM $TABLE_NAME WHERE $NAME_COl = '$name'",
            null)
        cur.moveToFirst()
        return cur.getString(2).toString()
    }
    fun updateItem(name: String, qty: String) {
        val values = ContentValues()
        values.put(QNT_COL, qty)
        val db = this.writableDatabase
        db.update(TABLE_NAME, values, NAME_COl + "=?", arrayOf(name))
    }
    fun delItem(name: String) {
        val db = this.writableDatabase
        db.delete(TABLE_NAME, NAME_COl + "=?", arrayOf(name))
    }
    fun getQty(): List<String>? {
        val db = this.readableDatabase
        var items = mutableListOf<String>()
        var cur = db.rawQuery("SELECT * FROM " + TABLE_NAME, null)
        if (cur.moveToFirst()) {
            while (cur.moveToNext()) {
                items.add(cur!!.getString(2))
            }
        }
        return items
    } }