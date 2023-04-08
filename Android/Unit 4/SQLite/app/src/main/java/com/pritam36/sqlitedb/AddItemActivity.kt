package com.pritam36.sqlitedb

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast

class AddItemActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_add_item)

        val save_btn: Button = findViewById(R.id.save_btn)
        val itemName: EditText = findViewById(R.id.edit_additemname)
        val itemQty: EditText = findViewById(R.id.edit_addqty)
        val db: DBHelper = DBHelper(this, null)
        save_btn.setOnClickListener {
            db.setItem(itemName.text.toString(), itemQty.text.toString())
            startActivity(Intent(this, MainActivity::class.java))
            Toast.makeText(this, "Item Added to the list", Toast.LENGTH_LONG).show()
            finish()
        }
    }
}