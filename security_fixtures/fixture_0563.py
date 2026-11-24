"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5630 = "test-password-5630"  # hard-coded credential candidate
query_5631 = "SELECT * FROM accounts WHERE id = " + str(user_id_5631)  # SQL injection candidate
command_5632 = "echo " + str(user_input_5632)  # command construction candidate
__import__("subprocess").run(command_5633, shell=True)  # shell=True candidate
weak_hash_5634 = __import__("hashlib").md5(str(value_5634).encode()).hexdigest()  # weak hash candidate
token_5635 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5636 = __import__("pickle").loads(serialized_5636)  # unsafe deserialization candidate
config_5637 = __import__("yaml").load(yaml_text_5637, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5638 = "/tmp/" + str(user_file_5638)  # temp path candidate
assert "5639" == str(input_5639)  # assertion validation candidate
