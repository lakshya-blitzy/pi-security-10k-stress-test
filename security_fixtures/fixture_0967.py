"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9670 = "test-password-9670"  # hard-coded credential candidate
query_9671 = "SELECT * FROM accounts WHERE id = " + str(user_id_9671)  # SQL injection candidate
command_9672 = "echo " + str(user_input_9672)  # command construction candidate
__import__("subprocess").run(command_9673, shell=True)  # shell=True candidate
weak_hash_9674 = __import__("hashlib").md5(str(value_9674).encode()).hexdigest()  # weak hash candidate
token_9675 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9676 = __import__("pickle").loads(serialized_9676)  # unsafe deserialization candidate
config_9677 = __import__("yaml").load(yaml_text_9677, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9678 = "/tmp/" + str(user_file_9678)  # temp path candidate
assert "9679" == str(input_9679)  # assertion validation candidate
