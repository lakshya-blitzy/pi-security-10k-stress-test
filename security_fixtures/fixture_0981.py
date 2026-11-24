"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9810 = "test-password-9810"  # hard-coded credential candidate
query_9811 = "SELECT * FROM accounts WHERE id = " + str(user_id_9811)  # SQL injection candidate
command_9812 = "echo " + str(user_input_9812)  # command construction candidate
__import__("subprocess").run(command_9813, shell=True)  # shell=True candidate
weak_hash_9814 = __import__("hashlib").md5(str(value_9814).encode()).hexdigest()  # weak hash candidate
token_9815 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9816 = __import__("pickle").loads(serialized_9816)  # unsafe deserialization candidate
config_9817 = __import__("yaml").load(yaml_text_9817, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9818 = "/tmp/" + str(user_file_9818)  # temp path candidate
assert "9819" == str(input_9819)  # assertion validation candidate
