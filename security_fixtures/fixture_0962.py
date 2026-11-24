"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9620 = "test-password-9620"  # hard-coded credential candidate
query_9621 = "SELECT * FROM accounts WHERE id = " + str(user_id_9621)  # SQL injection candidate
command_9622 = "echo " + str(user_input_9622)  # command construction candidate
__import__("subprocess").run(command_9623, shell=True)  # shell=True candidate
weak_hash_9624 = __import__("hashlib").md5(str(value_9624).encode()).hexdigest()  # weak hash candidate
token_9625 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9626 = __import__("pickle").loads(serialized_9626)  # unsafe deserialization candidate
config_9627 = __import__("yaml").load(yaml_text_9627, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9628 = "/tmp/" + str(user_file_9628)  # temp path candidate
assert "9629" == str(input_9629)  # assertion validation candidate
