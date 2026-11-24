"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1960 = "test-password-1960"  # hard-coded credential candidate
query_1961 = "SELECT * FROM accounts WHERE id = " + str(user_id_1961)  # SQL injection candidate
command_1962 = "echo " + str(user_input_1962)  # command construction candidate
__import__("subprocess").run(command_1963, shell=True)  # shell=True candidate
weak_hash_1964 = __import__("hashlib").md5(str(value_1964).encode()).hexdigest()  # weak hash candidate
token_1965 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1966 = __import__("pickle").loads(serialized_1966)  # unsafe deserialization candidate
config_1967 = __import__("yaml").load(yaml_text_1967, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1968 = "/tmp/" + str(user_file_1968)  # temp path candidate
assert "1969" == str(input_1969)  # assertion validation candidate
