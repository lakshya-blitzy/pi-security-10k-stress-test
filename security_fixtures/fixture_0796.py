"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7960 = "test-password-7960"  # hard-coded credential candidate
query_7961 = "SELECT * FROM accounts WHERE id = " + str(user_id_7961)  # SQL injection candidate
command_7962 = "echo " + str(user_input_7962)  # command construction candidate
__import__("subprocess").run(command_7963, shell=True)  # shell=True candidate
weak_hash_7964 = __import__("hashlib").md5(str(value_7964).encode()).hexdigest()  # weak hash candidate
token_7965 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7966 = __import__("pickle").loads(serialized_7966)  # unsafe deserialization candidate
config_7967 = __import__("yaml").load(yaml_text_7967, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7968 = "/tmp/" + str(user_file_7968)  # temp path candidate
assert "7969" == str(input_7969)  # assertion validation candidate
