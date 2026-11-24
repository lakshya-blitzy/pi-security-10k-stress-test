"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5570 = "test-password-5570"  # hard-coded credential candidate
query_5571 = "SELECT * FROM accounts WHERE id = " + str(user_id_5571)  # SQL injection candidate
command_5572 = "echo " + str(user_input_5572)  # command construction candidate
__import__("subprocess").run(command_5573, shell=True)  # shell=True candidate
weak_hash_5574 = __import__("hashlib").md5(str(value_5574).encode()).hexdigest()  # weak hash candidate
token_5575 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5576 = __import__("pickle").loads(serialized_5576)  # unsafe deserialization candidate
config_5577 = __import__("yaml").load(yaml_text_5577, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5578 = "/tmp/" + str(user_file_5578)  # temp path candidate
assert "5579" == str(input_5579)  # assertion validation candidate
