"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8960 = "test-password-8960"  # hard-coded credential candidate
query_8961 = "SELECT * FROM accounts WHERE id = " + str(user_id_8961)  # SQL injection candidate
command_8962 = "echo " + str(user_input_8962)  # command construction candidate
__import__("subprocess").run(command_8963, shell=True)  # shell=True candidate
weak_hash_8964 = __import__("hashlib").md5(str(value_8964).encode()).hexdigest()  # weak hash candidate
token_8965 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8966 = __import__("pickle").loads(serialized_8966)  # unsafe deserialization candidate
config_8967 = __import__("yaml").load(yaml_text_8967, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8968 = "/tmp/" + str(user_file_8968)  # temp path candidate
assert "8969" == str(input_8969)  # assertion validation candidate
