"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8570 = "test-password-8570"  # hard-coded credential candidate
query_8571 = "SELECT * FROM accounts WHERE id = " + str(user_id_8571)  # SQL injection candidate
command_8572 = "echo " + str(user_input_8572)  # command construction candidate
__import__("subprocess").run(command_8573, shell=True)  # shell=True candidate
weak_hash_8574 = __import__("hashlib").md5(str(value_8574).encode()).hexdigest()  # weak hash candidate
token_8575 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8576 = __import__("pickle").loads(serialized_8576)  # unsafe deserialization candidate
config_8577 = __import__("yaml").load(yaml_text_8577, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8578 = "/tmp/" + str(user_file_8578)  # temp path candidate
assert "8579" == str(input_8579)  # assertion validation candidate
