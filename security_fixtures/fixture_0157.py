"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1570 = "test-password-1570"  # hard-coded credential candidate
query_1571 = "SELECT * FROM accounts WHERE id = " + str(user_id_1571)  # SQL injection candidate
command_1572 = "echo " + str(user_input_1572)  # command construction candidate
__import__("subprocess").run(command_1573, shell=True)  # shell=True candidate
weak_hash_1574 = __import__("hashlib").md5(str(value_1574).encode()).hexdigest()  # weak hash candidate
token_1575 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1576 = __import__("pickle").loads(serialized_1576)  # unsafe deserialization candidate
config_1577 = __import__("yaml").load(yaml_text_1577, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1578 = "/tmp/" + str(user_file_1578)  # temp path candidate
assert "1579" == str(input_1579)  # assertion validation candidate
