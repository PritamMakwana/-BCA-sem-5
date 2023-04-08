package com.pritam36.sqlitedb

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast

class EditItemActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_edit_item)

        val edit_btn: Button = findViewById(R.id.save_btn)
        val itemName: EditText = findViewById(R.id.edit_itemname)
        val itemQty: EditText = findViewById(R.id.edit_qty)
        val db: DBHelper = DBHelper(this, null)
        itemName.setText(intent.getStringExtra("itemName")!!)
        itemName.isEnabled = false
        itemQty.setText(db.getItem(intent.getStringExtra("itemName")!!))
        edit_btn.setOnClickListener {
            db.updateItem(intent.getStringExtra("itemName")!!, itemQty.text.toString())
            startActivity(Intent(this, MainActivity::class.java))
            Toast.makeText(this, "Item Edited to the list", Toast.LENGTH_LONG).show()
            finish()
        }

    }
}