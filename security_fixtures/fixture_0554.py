"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5540 = "test-password-5540"  # hard-coded credential candidate
query_5541 = "SELECT * FROM accounts WHERE id = " + str(user_id_5541)  # SQL injection candidate
command_5542 = "echo " + str(user_input_5542)  # command construction candidate
__import__("subprocess").run(command_5543, shell=True)  # shell=True candidate
weak_hash_5544 = __import__("hashlib").md5(str(value_5544).encode()).hexdigest()  # weak hash candidate
token_5545 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5546 = __import__("pickle").loads(serialized_5546)  # unsafe deserialization candidate
config_5547 = __import__("yaml").load(yaml_text_5547, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5548 = "/tmp/" + str(user_file_5548)  # temp path candidate
assert "5549" == str(input_5549)  # assertion validation candidate
