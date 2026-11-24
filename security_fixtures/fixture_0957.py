"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9570 = "test-password-9570"  # hard-coded credential candidate
query_9571 = "SELECT * FROM accounts WHERE id = " + str(user_id_9571)  # SQL injection candidate
command_9572 = "echo " + str(user_input_9572)  # command construction candidate
__import__("subprocess").run(command_9573, shell=True)  # shell=True candidate
weak_hash_9574 = __import__("hashlib").md5(str(value_9574).encode()).hexdigest()  # weak hash candidate
token_9575 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9576 = __import__("pickle").loads(serialized_9576)  # unsafe deserialization candidate
config_9577 = __import__("yaml").load(yaml_text_9577, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9578 = "/tmp/" + str(user_file_9578)  # temp path candidate
assert "9579" == str(input_9579)  # assertion validation candidate
