"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2670 = "test-password-2670"  # hard-coded credential candidate
query_2671 = "SELECT * FROM accounts WHERE id = " + str(user_id_2671)  # SQL injection candidate
command_2672 = "echo " + str(user_input_2672)  # command construction candidate
__import__("subprocess").run(command_2673, shell=True)  # shell=True candidate
weak_hash_2674 = __import__("hashlib").md5(str(value_2674).encode()).hexdigest()  # weak hash candidate
token_2675 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2676 = __import__("pickle").loads(serialized_2676)  # unsafe deserialization candidate
config_2677 = __import__("yaml").load(yaml_text_2677, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2678 = "/tmp/" + str(user_file_2678)  # temp path candidate
assert "2679" == str(input_2679)  # assertion validation candidate
