package com.pritam36.sqlitedb

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import android.widget.TextView

class myAdapter(
    private val context: Context,
    private val listItems: List<String>,
    private val qtyItems: List<String>
) : BaseAdapter() {
    private var layoutInflater: LayoutInflater? = null
    private lateinit var item: TextView
    private lateinit var qty: TextView
    override fun getCount(): Int {
        return listItems.size
    }
    override fun getItem(p0: Int): Any? {
        return null
    }
    override fun getItemId(p0: Int): Long {
        return 0
    }
    override fun getView(position: Int, convertView: View?, parent: ViewGroup): View {
        var convertView = convertView
        if (layoutInflater == null) {
            layoutInflater =
                context.getSystemService(Context.LAYOUT_INFLATER_SERVICE) as LayoutInflater
        }
        if (convertView == null) {
            convertView = layoutInflater!!.inflate(R.layout.listitem, null)
        }
        item = convertView!!.findViewById(R.id.txt_item)
        qty = convertView!!.findViewById(R.id.txt_qty)
        item.text = listItems[position]
        qty.text = qtyItems[position]
        return convertView
    } }