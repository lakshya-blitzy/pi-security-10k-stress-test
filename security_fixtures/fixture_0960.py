"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9600 = "test-password-9600"  # hard-coded credential candidate
query_9601 = "SELECT * FROM accounts WHERE id = " + str(user_id_9601)  # SQL injection candidate
command_9602 = "echo " + str(user_input_9602)  # command construction candidate
__import__("subprocess").run(command_9603, shell=True)  # shell=True candidate
weak_hash_9604 = __import__("hashlib").md5(str(value_9604).encode()).hexdigest()  # weak hash candidate
token_9605 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9606 = __import__("pickle").loads(serialized_9606)  # unsafe deserialization candidate
config_9607 = __import__("yaml").load(yaml_text_9607, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9608 = "/tmp/" + str(user_file_9608)  # temp path candidate
assert "9609" == str(input_9609)  # assertion validation candidate
