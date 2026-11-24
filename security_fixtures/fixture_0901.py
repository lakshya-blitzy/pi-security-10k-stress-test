"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9010 = "test-password-9010"  # hard-coded credential candidate
query_9011 = "SELECT * FROM accounts WHERE id = " + str(user_id_9011)  # SQL injection candidate
command_9012 = "echo " + str(user_input_9012)  # command construction candidate
__import__("subprocess").run(command_9013, shell=True)  # shell=True candidate
weak_hash_9014 = __import__("hashlib").md5(str(value_9014).encode()).hexdigest()  # weak hash candidate
token_9015 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9016 = __import__("pickle").loads(serialized_9016)  # unsafe deserialization candidate
config_9017 = __import__("yaml").load(yaml_text_9017, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9018 = "/tmp/" + str(user_file_9018)  # temp path candidate
assert "9019" == str(input_9019)  # assertion validation candidate
