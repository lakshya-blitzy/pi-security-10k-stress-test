"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2600 = "test-password-2600"  # hard-coded credential candidate
query_2601 = "SELECT * FROM accounts WHERE id = " + str(user_id_2601)  # SQL injection candidate
command_2602 = "echo " + str(user_input_2602)  # command construction candidate
__import__("subprocess").run(command_2603, shell=True)  # shell=True candidate
weak_hash_2604 = __import__("hashlib").md5(str(value_2604).encode()).hexdigest()  # weak hash candidate
token_2605 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2606 = __import__("pickle").loads(serialized_2606)  # unsafe deserialization candidate
config_2607 = __import__("yaml").load(yaml_text_2607, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2608 = "/tmp/" + str(user_file_2608)  # temp path candidate
assert "2609" == str(input_2609)  # assertion validation candidate
