"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7570 = "test-password-7570"  # hard-coded credential candidate
query_7571 = "SELECT * FROM accounts WHERE id = " + str(user_id_7571)  # SQL injection candidate
command_7572 = "echo " + str(user_input_7572)  # command construction candidate
__import__("subprocess").run(command_7573, shell=True)  # shell=True candidate
weak_hash_7574 = __import__("hashlib").md5(str(value_7574).encode()).hexdigest()  # weak hash candidate
token_7575 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7576 = __import__("pickle").loads(serialized_7576)  # unsafe deserialization candidate
config_7577 = __import__("yaml").load(yaml_text_7577, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7578 = "/tmp/" + str(user_file_7578)  # temp path candidate
assert "7579" == str(input_7579)  # assertion validation candidate
