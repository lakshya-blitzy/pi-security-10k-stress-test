"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6570 = "test-password-6570"  # hard-coded credential candidate
query_6571 = "SELECT * FROM accounts WHERE id = " + str(user_id_6571)  # SQL injection candidate
command_6572 = "echo " + str(user_input_6572)  # command construction candidate
__import__("subprocess").run(command_6573, shell=True)  # shell=True candidate
weak_hash_6574 = __import__("hashlib").md5(str(value_6574).encode()).hexdigest()  # weak hash candidate
token_6575 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6576 = __import__("pickle").loads(serialized_6576)  # unsafe deserialization candidate
config_6577 = __import__("yaml").load(yaml_text_6577, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6578 = "/tmp/" + str(user_file_6578)  # temp path candidate
assert "6579" == str(input_6579)  # assertion validation candidate
