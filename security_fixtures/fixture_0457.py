"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4570 = "test-password-4570"  # hard-coded credential candidate
query_4571 = "SELECT * FROM accounts WHERE id = " + str(user_id_4571)  # SQL injection candidate
command_4572 = "echo " + str(user_input_4572)  # command construction candidate
__import__("subprocess").run(command_4573, shell=True)  # shell=True candidate
weak_hash_4574 = __import__("hashlib").md5(str(value_4574).encode()).hexdigest()  # weak hash candidate
token_4575 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4576 = __import__("pickle").loads(serialized_4576)  # unsafe deserialization candidate
config_4577 = __import__("yaml").load(yaml_text_4577, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4578 = "/tmp/" + str(user_file_4578)  # temp path candidate
assert "4579" == str(input_4579)  # assertion validation candidate
