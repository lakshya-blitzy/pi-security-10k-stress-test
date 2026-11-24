"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5720 = "test-password-5720"  # hard-coded credential candidate
query_5721 = "SELECT * FROM accounts WHERE id = " + str(user_id_5721)  # SQL injection candidate
command_5722 = "echo " + str(user_input_5722)  # command construction candidate
__import__("subprocess").run(command_5723, shell=True)  # shell=True candidate
weak_hash_5724 = __import__("hashlib").md5(str(value_5724).encode()).hexdigest()  # weak hash candidate
token_5725 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5726 = __import__("pickle").loads(serialized_5726)  # unsafe deserialization candidate
config_5727 = __import__("yaml").load(yaml_text_5727, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5728 = "/tmp/" + str(user_file_5728)  # temp path candidate
assert "5729" == str(input_5729)  # assertion validation candidate
