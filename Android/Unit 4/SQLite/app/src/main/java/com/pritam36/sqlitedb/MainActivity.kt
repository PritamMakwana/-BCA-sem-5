package com.pritam36.sqlitedb

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.AdapterView
import android.widget.Button
import android.widget.ListView

class MainActivity : AppCompatActivity() {

    lateinit var list: ListView
    lateinit var btn_addItem: Button
    var itemArray: List<String>? = null
    var qtyArray: List<String>? = null
    val db: DBHelper = DBHelper(this, null)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        list = findViewById(R.id.list)
        btn_addItem = findViewById(R.id.btn_additem)
        reset()
        btn_addItem.setOnClickListener {
            startActivity(Intent(this, AddItemActivity::class.java))
            finish()
        }
    }
    private fun reset() {
        itemArray = db.getItems()
        qtyArray = db.getQty()
        val mainAdapter = myAdapter(this, itemArray!!,qtyArray!!)
        list.adapter = mainAdapter
        list.onItemClickListener = AdapterView.OnItemClickListener { _, _,
                                                                     position, _ ->
            db.delItem(itemArray!![position])
            reset()
        }
        list.onItemLongClickListener = AdapterView.OnItemLongClickListener { _, _, position, _ ->
            startActivity(
                Intent(this, EditItemActivity::class.java).putExtra(
                    "itemName",
                    itemArray!![position]
                )
            )
            finish()
            true
        }
    } }